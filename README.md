
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/amitbiderman/screenshot_project">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Screenshot Program</h3>

  <p align="center">
   By Amit Biderman
  </p>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A dockerized python application, that takes in a URL and saves a screenshot of the desired URL on the host's machine.

### Built With

* <img src="https://img.icons8.com/dusk/30/000000/docker.png"/> [Docker](https://www.docker.com/m)
* <img src="https://img.icons8.com/color/30/000000/python.png"/> [Python](https://www.python.org/)
* <img src="https://img.icons8.com/officel/30/000000/selenium-test-automation.png"/> [Selenium]https://www.selenium.dev/)



<!-- GETTING STARTED -->
## Getting Started

You have two options to use it for your preference:

1. Clone this repository [Screenshot Project](https://github.com/amitbiderman/screenshot_project)
* Installing Git is required for this step

2. Pull Docker image from [Docker Hub](https://hub.docker.com/) 

For both of these options Docker is required (Steps for installation are specified below)

Both steps are explained below

### Installing Docker

1. Install Docker [Documentation link](https://docs.docker.com/get-docker/):

* Windows
[Download the latest Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
```sh
  Simply install after download is finished, restart your machine, and start the program.
  ```

* Linux Debian Using the Convenient Script
```sh
  $ url -fsSL https://get.docker.com -o get-docker.sh
  $ sudo sh get-docker.sh
  ```
  
* For other Linux Distributions Please Follow [This Link] (https://docs.docker.com/engine/install/)


* macOS
[Download the latest Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)
```sh
  Simply install after download is finished, restart your machine, and start the program.
  ```


### Cloning The Repository

If you don't have Git on your local machine:
* Windows
```sh
  [Direct Download Link] (https://git-scm.com/download/win )
  ```

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


* Create a new folder in your local machine.
* Clone the repository

* git clone
  ```sh
  git clone https://github.com/amitbiderman/screenshot_project.git
  ```

* Build the image (This could take a couple of minutes)
  ```sh
  docker build -t <Your Tag> .
  ```


### Pulling Image from Docker Hub

* Create a new folder in your local machine.
* Pull the image
  ```sh
  docker pull amitbiderman/mimecast_project:latest
  ```


<!-- USAGE EXAMPLES -->
## Usage
Since the purpose of the program is to go to a URL and take a screenshot, a URL is needed to be specified.

* You can either run the docker run command and specify volumes, image and URL at the end

If pulled image from DockerHub:
  ```sh
 docker run -v /app -v $(pwd):/app amitbiderman/mimecast_project <ENTER URL HERE>
  ```
If created your own image with the build command:
  ```sh
 docker run -v /app -v $(pwd):/app amitbiderman/mimecast_project <ENTER URL HERE>
  ```
  
  
* Or edit the docker-compose.yml file with your wanted URL and and simply run:

  ```sh
  $ docker-compose up
  ```
