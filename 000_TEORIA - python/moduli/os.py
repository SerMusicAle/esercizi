import os

# ===========================================
# Funzioni di Gestione dei File e delle Directory
# ===========================================

def example_chdir():
    """Cambia la directory corrente di lavoro al percorso specificato."""
    os.chdir('/path/to/directory')
    print("Changed directory to:", os.getcwd())

def example_getcwd():
    """Restituisce la directory corrente di lavoro."""
    current_dir = os.getcwd()
    print("Current working directory:", current_dir)

def example_listdir():
    """Restituisce un elenco di nomi di file e directory nel percorso specificato."""
    files_and_dirs = os.listdir('.')
    print("Files and directories:", files_and_dirs)

def example_mkdir():
    """Crea una nuova directory al percorso specificato."""
    os.mkdir('new_directory')
    print("Created directory: new_directory")

def example_makedirs():
    """Crea tutte le directory intermedie necessarie per creare il percorso specificato."""
    os.makedirs('parent_dir/child_dir', exist_ok=True)
    print("Created directories: parent_dir/child_dir")

def example_remove():
    """Elimina il file specificato."""
    os.remove('file_to_delete.txt')
    print("Removed file: file_to_delete.txt")

def example_rmdir():
    """Elimina la directory specificata."""
    os.rmdir('empty_directory')
    print("Removed directory: empty_directory")

def example_removedirs():
    """Elimina directory vuote ricorsivamente."""
    os.removedirs('parent_dir/child_dir')
    print("Removed directories: parent_dir/child_dir")

def example_rename():
    """Rinomina il file o la directory da src a dst."""
    os.rename('old_name.txt', 'new_name.txt')
    print("Renamed file from old_name.txt to new_name.txt")

def example_replace():
    """Sostituisce dst con src, rinominando e sovrascrivendo se necessario."""
    os.replace('old_name.txt', 'new_name.txt')
    print("Replaced file: old_name.txt with new_name.txt")

def example_stat():
    """Restituisce le informazioni di stato del percorso specificato."""
    file_info = os.stat('example.txt')
    print("File stats for example.txt:", file_info)

def example_symlink():
    """Crea un collegamento simbolico che punta da dst a src."""
    os.symlink('source.txt', 'symlink.txt')
    print("Created symlink: symlink.txt -> source.txt")

def example_link():
    """Crea un hard link che punta da dst a src."""
    os.link('source.txt', 'hardlink.txt')
    print("Created hard link: hardlink.txt -> source.txt")

def example_unlink():
    """Rimuove il file specificato (alias di os.remove())."""
    os.unlink('file_to_delete.txt')
    print("Unlinked (removed) file: file_to_delete.txt")

def example_access():
    """Verifica se il percorso è accessibile."""
    can_read = os.access('example.txt', os.R_OK)
    print("Can read example.txt?", can_read)

def example_chmod():
    """Cambia i permessi del file."""
    os.chmod('example.txt', 0o644)
    print("Changed permissions of example.txt to 644")

def example_chown():
    """Cambia l'utente e il gruppo proprietari del file."""
    os.chown('example.txt', 1000, 1000)  # Esempio con UID e GID 1000
    print("Changed owner and group of example.txt to 1000")

def example_makedirs_exist_ok():
    """Crea una directory e tutte le directory intermedie, se non esistono già."""
    os.makedirs('path/to/dir', exist_ok=True)
    print("Created directories with exist_ok=True")

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_chdir()
    example_getcwd()
    example_listdir()
    example_mkdir()
    example_makedirs()
    example_remove()
    example_rmdir()
    example_removedirs()
    example_rename()
    example_replace()
    example_stat()
    example_symlink()
    example_link()
    example_unlink()
    example_access()
    example_chmod()
    example_chown()
    example_makedirs_exist_ok()



# ===========================================
# Funzioni di Gestione del Percorso
# ===========================================

def example_abspath():
    """Restituisce il percorso assoluto."""
    abs_path = os.path.abspath('example.txt')
    print("Absolute path of example.txt:", abs_path)

def example_basename():
    """Restituisce il nome base del percorso."""
    base_name = os.path.basename('/path/to/file.txt')
    print("Base name of /path/to/file.txt:", base_name)

def example_dirname():
    """Restituisce la directory del percorso."""
    dir_name = os.path.dirname('/path/to/file.txt')
    print("Directory name of /path/to/file.txt:", dir_name)

def example_exists():
    """Restituisce True se il percorso esiste."""
    exists = os.path.exists('example.txt')
    print("Does example.txt exist?", exists)

def example_isfile():
    """Restituisce True se il percorso è un file."""
    is_file = os.path.isfile('example.txt')
    print("Is example.txt a file?", is_file)

def example_isdir():
    """Restituisce True se il percorso è una directory."""
    is_dir = os.path.isdir('/path/to/directory')
    print("Is /path/to/directory a directory?", is_dir)

def example_islink():
    """Restituisce True se il percorso è un collegamento simbolico."""
    is_link = os.path.islink('symlink.txt')
    print("Is symlink.txt a symbolic link?", is_link)

def example_ismount():
    """Restituisce True se il percorso è un punto di montaggio."""
    is_mount = os.path.ismount('/mnt')
    print("Is /mnt a mount point?", is_mount)

def example_join():
    """Unisce più componenti di percorso in uno solo."""
    joined_path = os.path.join('/path', 'to', 'file.txt')
    print("Joined path:", joined_path)

def example_normpath():
    """Normalizza il percorso, eliminando i separatori di directory ridondanti."""
    normalized_path = os.path.normpath('/path//to///file.txt')
    print("Normalized path:", normalized_path)

def example_realpath():
    """Restituisce il percorso canonico del file."""
    real_path = os.path.realpath('symlink.txt')
    print("Real path of symlink.txt:", real_path)

def example_relpath():
    """Restituisce il percorso relativo dal percorso start."""
    rel_path = os.path.relpath('/path/to/file.txt', '/path')
    print("Relative path from /path to /path/to/file.txt:", rel_path)

def example_split():
    """Divide il percorso in una tupla di (head, tail)."""
    split_path = os.path.split('/path/to/file.txt')
    print("Split path of /path/to/file.txt:", split_path)

def example_splitext():
    """Divide il percorso in una tupla di (root, ext)."""
    split_ext = os.path.splitext('file.txt')
    print("Split extension of file.txt:", split_ext)

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_abspath()
    example_basename()
    example_dirname()
    example_exists()
    example_isfile()
    example_isdir()
    example_islink()
    example_ismount()
    example_join()
    example_normpath()
    example_realpath()
    example_relpath()
    example_split()
    example_splitext()



# ===========================================
# Funzioni di Gestione degli Errori
# ===========================================

def example_os_error():
    """Classe base per le eccezioni del modulo os."""
    try:
        os.remove('non_existent_file.txt')
    except os.error as e:
        print(f"Errore: {e}")
        # Output: Errore: [Errno 2] No such file or directory: 'non_existent_file.txt'

def example_strerror():
    """Restituisce la stringa di errore corrispondente al numero di errore specificato."""
    error_message = os.strerror(2)
    print("Error message for code 2:", error_message)
    # Output: Error message for code 2: No such file or directory

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_os_error()
    example_strerror()




# ===========================================
# Funzioni di Ambiente
# ===========================================

def example_environ():
    """Dizionario delle variabili d'ambiente."""
    env_vars = os.environ
    print("Environment variables:", env_vars)
    # Output: Environment variables: environ({'PATH': '...', ...})

def example_getenv():
    """Restituisce il valore della variabile d'ambiente key."""
    path_value = os.getenv('PATH')
    print("PATH environment variable:", path_value)
    # Output: PATH environment variable: <actual PATH value>

def example_putenv():
    """Imposta la variabile d'ambiente key a value."""
    os.putenv('MY_VAR', 'value')
    print("Set environment variable MY_VAR to 'value'")
    # Note: os.putenv may not update os.environ directly on some platforms

def example_unsetenv():
    """Rimuove la variabile d'ambiente key."""
    os.unsetenv('MY_VAR')
    print("Unset environment variable MY_VAR")
    # Note: os.unsetenv may not update os.environ directly on some platforms

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_environ()
    example_getenv()
    example_putenv()
    example_unsetenv()


# ===========================================
# Funzioni di Gestione dei Processi
# ===========================================

def example_system():
    """Esegue il comando nel sistema operativo."""
    os.system('echo Hello, World!')
    print("Executed system command: echo Hello, World!")
    # Output: Executed system command: echo Hello, World!

def example_popen():
    """Esegue il comando e apre un flusso."""
    with os.popen('echo Hello, World!') as stream:
        output = stream.read()
        print("Output from popen command:", output)
        # Output: Output from popen command: Hello, World!

def example_spawnv():
    """Crea un nuovo processo."""
    pid = os.spawnv(os.P_NOWAIT, '/bin/echo', ['echo', 'Hello, World!'])
    print(f"Spawned new process with PID: {pid}")
    # Output: Spawned new process with PID: <PID>

def example_spawnve():
    """Crea un nuovo processo con variabili d'ambiente specificate."""
    pid = os.spawnve(os.P_NOWAIT, '/bin/echo', ['echo', 'Hello, World!'], os.environ)
    print(f"Spawned new process with PID: {pid} using custom environment")
    # Output: Spawned new process with PID: <PID> using custom environment

def example_getpid():
    """Restituisce l'ID del processo corrente."""
    pid = os.getpid()
    print(f"Current process ID: {pid}")
    # Output: Current process ID: <PID>

def example_getppid():
    """Restituisce l'ID del processo padre."""
    ppid = os.getppid()
    print(f"Parent process ID: {ppid}")
    # Output: Parent process ID: <PPID>

def example_wait():
    """Attende il completamento di un processo figlio."""
    pid = os.spawnv(os.P_NOWAIT, '/bin/sleep', ['sleep', '1'])
    print(f"Waiting for process {pid} to complete")
    completed_pid, status = os.wait()
    print(f"Process {completed_pid} completed with status {status}")
    # Output: Waiting for process <PID> to complete
    # Process <PID> completed with status <Status>

def example_exit():
    """Termina immediatamente il processo con il codice di stato specificato."""
    print("Exiting with status 0")
    os._exit(0)
    # Output: (Terminates process, no further output)

# Nota: Le seguenti funzioni sostituiscono il processo corrente con un nuovo processo, quindi sono commentate.
# def example_execv():
#     """Sostituisce il processo corrente con un nuovo processo."""
#     os.execv('/bin/ls', ['ls'])
#     # Non ritorna: sostituisce il processo corrente

# def example_execve():
#     """Come os.execv, ma accetta anche l'ambiente del nuovo processo."""
#     os.execve('/bin/ls', ['ls'], os.environ)
#     # Non ritorna: sostituisce il processo corrente

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_system()
    example_popen()
    example_spawnv()
    example_spawnve()
    example_getpid()
    example_getppid()
    example_wait()
    # example_exit()  # Commentato per evitare l'uscita immediata

# ===========================================
# Funzioni di Gestione degli ID e Permessi
# ===========================================

def example_getpid():
    """Restituisce l'ID del processo corrente."""
    pid = os.getpid()
    print("Current process ID:", pid)
    # Output: Current process ID: <PID>

def example_getppid():
    """Restituisce l'ID del processo padre."""
    ppid = os.getppid()
    print("Parent process ID:", ppid)
    # Output: Parent process ID: <PPID>

def example_getuid():
    """Restituisce l'ID utente effettivo del processo corrente (Unix)."""
    uid = os.getuid()
    print("Effective user ID:", uid)
    # Output: Effective user ID: <UID>

def example_getgid():
    """Restituisce l'ID gruppo effettivo del processo corrente (Unix)."""
    gid = os.getgid()
    print("Effective group ID:", gid)
    # Output: Effective group ID: <GID>

def example_setuid():
    """Imposta l'ID utente effettivo del processo corrente (Unix)."""
    try:
        os.setuid(1000)  # Questo ID deve essere valido e l'esecuzione richiede privilegi di root
        print("User ID set to 1000")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    # Output: PermissionError: [Errno 1] Operation not permitted

def example_setgid():
    """Imposta l'ID gruppo effettivo del processo corrente (Unix)."""
    try:
        os.setgid(1000)  # Questo ID deve essere valido e l'esecuzione richiede privilegi di root
        print("Group ID set to 1000")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    # Output: PermissionError: [Errno 1] Operation not permitted

def example_umask():
    """Imposta la maschera di creazione dei permessi per i nuovi file."""
    old_umask = os.umask(0o022)
    print(f"Old umask: {oct(old_umask)}")
    # Output: Old umask: 0o<vecchia_umask>

# Nota: Le seguenti funzioni richiedono privilegi di amministratore e sono per ambienti Unix.

def example_chmod():
    """Cambia i permessi di accesso al percorso specificato."""
    os.chmod('example.txt', 0o644)
    print("Changed permissions of example.txt to 644 (rw-r--r--)")
    # Output: Changed permissions of example.txt to 644 (rw-r--r--)

def example_chown():
    """Cambia il proprietario e il gruppo del percorso specificato (Unix)."""
    try:
        os.chown('example.txt', 1000, 1000)  # IDs di esempio per utente e gruppo
        print("Changed owner and group of example.txt to 1000:1000")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    # Output: PermissionError: [Errno 1] Operation not permitted

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_getpid()
    example_getppid()
    example_getuid()
    example_getgid()
    example_umask()
    example_chmod()
    example_chown()
    # example_setuid()  # Commentato per evitare errori su ambienti non root
    # example_setgid()  # Commentato per evitare errori su ambienti non root



# ===========================================
# Altre Funzioni Utili
# ===========================================

def example_cpu_count():
    """Restituisce il numero di CPU nel sistema."""
    cpu_count = os.cpu_count()
    print("Number of CPUs:", cpu_count)
    # Output: Number of CPUs: <numero_di_cpu>

def example_urandom():
    """Restituisce una stringa di byte casuali."""
    random_bytes = os.urandom(16)
    print("Random bytes:", random_bytes)
    # Output: Random bytes: b'<16_byte_casuali>'

def example_name():
    """Restituisce il nome del sistema operativo in uso ('posix', 'nt', ecc.)."""
    os_name = os.name
    print("Operating system name:", os_name)
    # Output: Operating system name: 'posix' o 'nt'

def example_dup():
    """Duplica il descrittore di file."""
    with open('example.txt', 'w') as f:
        fd = f.fileno()
        fd_copy = os.dup(fd)
        print("Duplicated file descriptor:", fd_copy)
        # Output: Duplicated file descriptor: <file_descriptor_copiato>

def example_dup2():
    """Duplica fd in fd2."""
    with open('example.txt', 'w') as f:
        fd = f.fileno()
        fd_copy = 10  # Scegli un file descriptor disponibile
        os.dup2(fd, fd_copy)
        print(f"Duplicated file descriptor {fd} to {fd_copy}")
        # Output: Duplicated file descriptor <fd> to <fd_copy>

def example_getloadavg():
    """Restituisce il carico medio di sistema negli ultimi 1, 5 e 15 minuti (Unix)."""
    try:
        load_avg = os.getloadavg()
        print("System load average:", load_avg)
        # Output: System load average: (<1_min_load>, <5_min_load>, <15_min_load>)
    except AttributeError:
        print("Function not supported on this operating system.")

def example_ctermid():
    """Restituisce il nome del terminale di controllo del processo."""
    try:
        termid = os.ctermid()
        print("Control terminal name:", termid)
        # Output: Control terminal name: /dev/tty
    except AttributeError:
        print("Function not supported on this operating system.")

# ===========================================
# Esempi di chiamata alle funzioni
# ===========================================

if __name__ == "__main__":
    example_cpu_count()
    example_urandom()
    example_name()
    example_dup()
    example_dup2()
    example_getloadavg()
    example_ctermid()

