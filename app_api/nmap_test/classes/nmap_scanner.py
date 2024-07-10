from subprocess import run


class NmapScanner:
    def __init__(self, ip: str, nmap: str, options: list[str]):
        self.ip = ip
        self.nmap = nmap
        self.options = options

    def scan(self) -> str:
        command = [self.nmap] + self.options + [self.ip]
        result = run(command, capture_output=True, text=True)
        return result.stdout
