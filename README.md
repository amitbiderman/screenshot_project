
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/amitbiderman/screenshot_project">
    <img src="images/logo.png" alt="Logo" width="400" height="400">
  </a>

  <h3 align="center">Screenshot Program</h3>

  <p align="center">
   By Amit Biderman
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

  <a href="https://github.com/amitbiderman/screenshot_project">
    <img src="images/graph.jpg" alt="Logo" width="874" height="396">
  </a>

A dockerized python application, that takes in a URL and saves a screenshot of the desired URL on the host's machine.

### Built With

* <img src="https://img.icons8.com/dusk/30/000000/docker.png"/> [Docker](https://www.docker.com/m)
* <img src="https://img.icons8.com/color/30/000000/python.png"/> [Python](https://www.python.org/)
* <img src="https://img.icons8.com/officel/30/000000/selenium-test-automation.png"/> [Selenium](https://www.selenium.dev/)



<!-- GETTING STARTED -->
## Getting Started

You have two options to use it for your preference:

1. Build Your Image.

For this option Git is required.

2. Pull Docker image from [Docker Hub](https://hub.docker.com/) 

For both of these options Docker installation is required.


### Installing Docker

Install Docker [Documentation link](https://docs.docker.com/get-docker/):

* Windows
[Download the latest Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

Simply install after download is finished, restart your machine, and start the program.


* Linux Debian Using the Convenient Script
```sh
  $ url -fsSL https://get.docker.com -o get-docker.sh
  $ sudo sh get-docker.sh
  ```
  
For other Linux Distributions Please Follow [This Link] (https://docs.docker.com/engine/install/)


* macOS
[Download the latest Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)

Simply install after download is finished, restart your machine, and start the program.

### Installing Git

* Windows

[Direct Download Link](https://git-scm.com/download/win)


* Linux Debian
```sh
  $ sudo apt install git-all
  ```
* Other Linux RPM-based Distributions
```sh
  $ sudo dnf install git-all
  ```
* macOS
```sh
  $ git --version
  ```

### Build you image


1. Create a new folder in your local machine.
2. Clone the repository
  ```sh
  git clone https://github.com/amitbiderman/screenshot_project.git
  ```

3. Build the image (This could take a couple of minutes)
  ```sh
  docker build -t <Your Image Name:Your Tag> .
  ```


### Pulling Image from Docker Hub

1. Create a new folder in your local machine.
2. Pull the image
  ```sh
  docker pull amitbiderman/mimecast_project_fix:latest
  ```


<!-- USAGE EXAMPLES -->
## Usage
Since the purpose of the program is to go to a URL and take a screenshot, a URL is needed to be specified.

That can be achieved using either docker run command, or taking advantage of the docker-compose file.

## Use docker run command

run the docker run command and specify volumes, image and URL at the end

If pulled image from DockerHub:
  ```sh
 docker run -v /app/screenshot -v $(pwd):/app/screenshot amitbiderman/mimecast_project_fix <ENTER URL HERE>
  ```
If you created your own image:
  ```sh
 docker run -v /app/screenshot -v $(pwd):/app/screenshot <Your Image name:Your tag> <ENTER URL HERE>
  ```
  
 
 ## Use docker-compose up command (docker-compose file must be in project repository for this option!)
 
1. Edit the docker-compose.yml file with your wanted URL: (replace youtube.com in the example with YOUR wanted URL !)

<a href="https://github.com/amitbiderman/screenshot_project">
    <img src="images/docker-compose.png" alt="Logo" width="594" height="266">
  </a>

File content for easy copy:
```sh
version: '3'
services:
  mimecast_project:
    image: amitbiderman/mimecast_project_fix
    volumes:
      - ".:/app"
    command: youtube.com
```


2. And then  simply run:

  ```sh
  $ docker-compose up
  ```
  
  ## Congratulations! Your image is now in your project directory!
