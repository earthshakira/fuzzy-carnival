# MP-TCP vs MP-QUIC

In the first phase, we are just trying to create an environment to facilitate the simulation of both the protocols and help in the setup, assesment and manipulation of the underlying network setups in each case.
## Mininet

1. Setting up Mininet (**Ubuntu**)

```
	run bash mininet_setup.sh
```

**Note:** Just __DON'T__ Do it

2. Use The mininet VM

## References

https://www.usenix.org/system/files/conference/nsdi14/nsdi14-paper-singla.pdf
https://github.com/mininet/mininet/wiki/pdf/mininet-presentation-2009.pdf
https://github.com/mininet/mininet/wiki/Simple-Router 

## MPTCP

1. Use [Ubuntu 14.04](https://sourceforge.net/projects/osboxes/files/v/vb/55-U-u/14.04/14.04.6/1404-664.7z/download) and install [MPTCP](https://multipath-tcp.org/pmwiki.php/Users/AptRepository) (use the older releases in the)
```
	Q: Why Ubuntu 14.04 isn't the current version 18.0x.
	A: Because The mininet VM we are gonna use to test it is going to be 14.04

	Q: Why do we need the mininet VM can't we just set it up in the newer Ubuntu VM by ourselves.
	A: We can, but what about MPQUIC, how do we implement it? There is an existing implementation based on the Mininet VM.
```