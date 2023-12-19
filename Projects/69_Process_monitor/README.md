# Process monitor

This project consists of a Python process monitor that uses the `psutil` module to display information about running processes. Additionally, demonstrate how to run two Python processes inside a Docker container.

## :information_source: Technologies used

- Docker
- Python

## :information_source: How to use?
```bash
# Clone the repository
$ git clone https://github.com/kurogai/100-redteam-projects.git

# Enter the repository
$ cd 100-redteam-projects/Projects/69_Process_monitor/

# Open a terminal and run
$ docker-compose up --build
```

## Project Structure

- **main.py:** Main Python file that lists information about processes.
- **server.py:** Python file responsible for a test server.
- **start.sh:** Startup script that starts both processes inside the Docker container.
- **Dockerfile:** Docker configuration file to create the container image.
- **docker-compose.yml:** Docker Compose configuration file to make it easier to run both processes.

## Usage

After running `docker-compose up --build`, the container will be started and the `server.py` and `main.py` processes will run inside the container. You can access information about processes through the `main.py` file or other services within the same Docker environment.


## Developer

<p align="center">
<a href="https://github.com/AugustoSavi" target="blank"><img align="center" src="https://avatars.githubusercontent.com/u/32443720?v=4" alt="Manthan" height="100" width="100" /></a>
</p>
