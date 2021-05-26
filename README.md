# Speedrun Server

This is a 1.16.1 vanilla speedrun-optimized server with scripts used to optimize the resetting process
with seed-input options for FSG.

## Usage

To use it just run the reset.sh shell script. If you want to run a particular seed (for FSG), pass it
in as an argument. If no argument is given it will leave the seed blank.

Ex: `./reset.sh 2483313382402348964`

## Requirements

- Python 3.8
- Java
- Some way to run shell scripts

## Reccomended Setup

I use Google Cloud Platform's compute engine with a virtual machine running Linux. I have 32GBs of RAM
and 8 vCPUs (make sure to choose compute-optimized) to speedup the world creation time, but change
jvmArgs.txt to be whatever works for you.

If you're a technical person I'd look into GCP's $300 free credits, you can set up a pretty great server,
and as long as you stop if after youre done playing, you can very resonably pay nothing for it.
