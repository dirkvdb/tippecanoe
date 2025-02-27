#!/usr/bin/env python3
import os
import sys
import sysconfig
import argparse

from deps.vcpkg.scripts.buildtools import vcpkg

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Bootstrap tileserver.",
            parents=[vcpkg.bootstrap_argparser()],
        )
        args = parser.parse_args()

        platform = sysconfig.get_platform()
        triplet = args.triplet
        if platform == "win-amd64":
            args.ui_enabled = True
            triplet = "x64-windows-static-vs2022"
        elif platform == "mingw":
            triplet = "x64-mingw"
        elif not triplet:
            triplet = vcpkg.prompt_for_triplet()

        if args.parent:
            del vcpkg
            sys.path.insert(0, os.path.join("..", "vcpkg-ports", "scripts"))
            from buildtools import vcpkg

        if args.clean:
            vcpkg.clean(triplet=triplet)
        else:
            vcpkg.bootstrap(ports_dir=os.path.join(".", "deps"), triplet=triplet, clean_after_build=args.clean_after_build)
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(-1)
    except RuntimeError as e:
        print(e)
        sys.exit(-1)
