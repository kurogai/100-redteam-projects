package Projects.Simple_port_scanner;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class PortScanner {

    public static void main(String[] args) {
        // verification if has ip target 
        if(args.length == 1){
            String ipTarget = args[0];
            List openPorts = portScan(ipTarget);
            openPorts.forEach(port -> System.out.println(ipTarget + ", port open: " + port));
        }
        else {
            System.out.println("Correct usage: script, IP address target");
            System.exit(0);
        }
    }

    public static List portScan(String ip) {
        ConcurrentLinkedQueue openPorts = new ConcurrentLinkedQueue<>();
        ExecutorService executorService = Executors.newFixedThreadPool(50);
        AtomicInteger port = new AtomicInteger(0);
        while (port.get() < 65535) {
            final int currentPort = port.getAndIncrement();
            executorService.submit(() -> {
                try {
                    Socket socket = new Socket();
                    // try connection
                    socket.connect(new InetSocketAddress(ip, currentPort), 200);
                    socket.close();
                    // if Connection established add to ConcurrentLinkedQueue
                    openPorts.add(currentPort);
                }
                catch (IOException e) {
                }

            });
        }
        executorService.shutdown();
        try {
            executorService.awaitTermination(10, TimeUnit.MINUTES);
        }
        catch (InterruptedException e) {
            e.printStackTrace();
        }

        List openPortList = new ArrayList<>();
        System.out.println("open Ports Queue: " + openPorts.size());
        while (!openPorts.isEmpty()) {
            // after verify turns ConcurrentLinkedQueue into List
            openPortList.add(openPorts.poll());
        }
        return openPortList;
    }

}