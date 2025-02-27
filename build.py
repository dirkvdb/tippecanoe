#!/usr/bin/env python3
import os
import sys
import sysconfig
import platform
import argparse
import importlib

from deps.vcpkg.scripts.buildtools import vcpkg

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Build tileserver.", parents=[vcpkg.build_argparser()]
        )

        parser.add_argument(
            "--build-config",
            dest="build_config",
            help="Build configuration (Debug or Release)",
            default="Release",
        )

        args = parser.parse_args()
        sys_platform = sysconfig.get_platform()

        triplet = args.triplet
        if sys_platform == "win-amd64":
            triplet = "x64-windows-static-vs2022"
        elif sys_platform == "mingw":
            triplet = "x64-mingw"
        elif not triplet:
            triplet = vcpkg.prompt_for_triplet()

        build_dir = "tileserver"
        if sys_platform != "win-amd64":
            build_dir += "-" + args.build_config.lower()
        vcpkg_root = os.path.join(".", "deps", "vcpkg", "installed", triplet, "tools")

        if args.parent:
            del vcpkg
            sys.path.insert(0, os.path.join("..", "vcpkg-ports", "scripts"))
            from buildtools import vcpkg

            vcpkg_root = os.path.join(
                "..", "vcpkg-ports", "installed", triplet, "tools"
            )

        cmake_args = ["-DBUILD_TESTING=ON"]

        if args.build_dist:
            vcpkg.build_project_release(
                os.path.abspath(args.source_dir),
                triplet=triplet,
                cmake_args=cmake_args,
                build_name=build_dir,
                targets=["package"],
                build_config=args.build_config,
                run_tests_after_build=args.run_tests,
            )
        else:
            vcpkg.build_project(
                os.path.abspath(args.source_dir),
                triplet=triplet,
                cmake_args=cmake_args,
                build_name=build_dir,
                build_config=args.build_config,
                run_tests_after_build=args.run_tests,
            )
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(-1)
    except RuntimeError as e:
        print(e)
        sys.exit(-1)
