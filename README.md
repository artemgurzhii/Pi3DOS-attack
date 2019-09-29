# PI3DoS attack

## Description

This attack destroys everything on it's way.

PI3DoS attack stands for
  - **PI** - TCP packet configuration is based on the first 100_000 numbers of the [Pi](https://en.wikipedia.org/wiki/Pi)
  - **3** - TCP's 3-way handshake
  - **DoS** - Denial Of Service

This DoS attack is an implementation of the **SYN Flood Attack**.
Here is a diagram of how it works ![syn flood diagram](https://www.cloudflare.com/img/learning/ddos/syn-flood-ddos-attack/syn-flood-attack-ddos-attack-diagram-2.png)
For more info visit [syn flood ddos attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)
First 100_000 numbers of the PI are received from the [PI.txt file](https://github.com/artemgurzhii/Pi3DOS-attack/blob/master/PI.txt)

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Python](https://www.python.org/)
* [Pipenv](https://github.com/pypa/pipenv#installation)

## Installation

* `git clone https://github.com/artemgurzhii/Pi3DOS-attack` this repository
* `cd Pi3DOS-attack`
* `pipenv install`
* `sudo python3 main.py`

## Acknowledgments

[Artiikk](https://github.com/Artiikk)
[sawezx](https://github.com/sawezx)
