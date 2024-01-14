import psutil

def listar_informacoes_processos():
    # Lista de itens desejados
    itens = [
        'cmdline', 
        'connections',
        'cpu_affinity', 
        'cpu_num', 
        'cpu_percent', 
        'cpu_times', 
        'create_time', 
        'cwd', 
        'environ', 
        'exe', 
        'gids', 
        'io_counters', 
        'ionice', 
        'memory_full_info', 
        'memory_info', 
        # 'memory_maps', 
        'memory_percent', 
        'name', 
        'nice', 
        'num_ctx_switches', 
        'num_fds', 
        'num_threads', 
        'open_files', 
        'pid', 
        'ppid', 
        'status', 
        'terminal', 
        'threads', 
        'uids', 
        'username'
    ]

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.as_dict(attrs=itens)
            print('\n---------------------------------------------------------------------------------------\n')

            print(f"\nPID: {process_info['pid']} - Nome: {process_info['name']}")
            print("Informações:")
            for item, value in process_info.items():
                if item not in ['pid', 'name']:
                    print(f"  {item}: {value}")

            print('\n---------------------------------------------------------------------------------------\n')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    listar_informacoes_processos()
