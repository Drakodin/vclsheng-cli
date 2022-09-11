import argparse
import sys
from constants.messages import ARG_ERROR_MESSAGE, VERSION

from operations.execution import run

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
    parser.add_argument(
        "-u",
        "--url",
        help="URL to input file. URLs provided need to have full public access.",
        dest="url",
        type=str
    )

    parser.add_argument(
        "-i",
        "--input-path",
        help="Local path to input file. This supersedes URL loading and thus if provided, -u args will be ignored.",
        dest="input_path",
        type=str
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Flag for more verbose reports. Enabling this enables all optional detail injections.",
        dest="verbose",
        action="store_true",
        default=False
    )

    parser.add_argument(
        "-a",
        "--audio-specs",
        help="Flag to add audio details to final report.",
        dest="audio_spec",
        action="store_true",
        default=False
    )

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show help text and exit."
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Show CLI version text and exit.",
        version=f"v{VERSION}"
    )

    try:
        args = parser.parse_args()
        run(
            args.url,
            args.input_path,
            args.verbose,
            args.audio_spec
        )
    except argparse.ArgumentError as error:
        sys.stderr.write(error.message)
        sys.stderr.write(ARG_ERROR_MESSAGE)
        parser.print_help()
