# TheHarvester Parser

This script parses JSON output files from TheHarvester and extracts specified sections of the data. It supports extracting hosts, emails, IPs, URLs, and ASNs. For hosts, it can optionally extract only the hostname.

## Features

- Extract specific sections from TheHarvester JSON output: hosts, emails, IPs, URLs, and ASNs.
- Optionally extract only the hostname from the hosts section, omitting the trailing IP, `:`, and trailing `.`.

## Usage

### Command-Line Arguments

- `-i`, `--input`: Input JSON file from TheHarvester (required).
- `-t`, `--target`: Target section to extract. Supported targets: `hosts`, `emails`, `ips`, `urls`, `asns` (required).
- `--only-hostname`: Only extract the hostname (without trailing IP, `:`, or trailing `.`) when the target is `hosts` (optional).

### Example Usage

1. **Extracting Hosts:**

    ```
    python theharvesterparser.py -i example.json -t hosts
    ```

2. **Extracting Emails:**

    ```
    python theharvesterparser.py -i example.json -t emails
    ```

3. **Extracting Hosts with Only Hostnames:**

    ```
    python theharvesterparser.py -i example.json -t hosts --only-hostname
    ```

### Example Output

#### Hosts
```
host1.example.com:93.184.216.34
host2.example.net:203.0.113.5
```

#### Hosts with --only-hostname
```
host1.example.com
host2.example.net
```

#### Emails
```
admin@example.com
support@example.net
```

#### IPs
```
93.184.216.34
203.0.113.5
```

#### URLs
```
http://example.com
https://example.net
```

#### ASNs
```
AS12345
AS67890
```

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/sam-hilliard/theharvesterparser.git
    cd theharvesterparser
    ```

2. Ensure you have Python installed (version 3.6 or later).

## Requirements

- Python 3.6+
- No additional packages are required (uses standard library).

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
