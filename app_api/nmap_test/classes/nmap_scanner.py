from subprocess import run


class NmapScanner:
    """
    A class to represent a Nmap scanner.

    Attributes
    ----------
    ip : str
        The IP address to scan.
    nmap : str
        The path to the Nmap executable.
    options : list[str]
        A list of options to pass to the Nmap command.
    """

    def __init__(self, ip: str, nmap: str, options: list[str]):
        """
        Constructs all the necessary attributes for the NmapScanner object.

        Parameters:
        ----------
        :param ip:
            The IP address to scan.
        :param nmap:
            The path to the Nmap executable.
        :param options:
            A list of options to pass to the Nmap command.
        """
        self.ip = ip
        self.nmap = nmap
        self.options = options

    def scan(self) -> str:
        """
        Runs the Nmap scan with the provided options on the given IP address.

        :return: str
            The output of Nmap scan.
        """
        # Constract the command to run with the provided options and IP address
        command = [self.nmap] + self.options + [self.ip]

        # Execute the command and capture the output.
        result = run(command, capture_output=True, text=True)

        # Return the standard output from the Nmap command
        return result.stdout
