import spiro
import spiroanimator


def main():
    print("generating spirograph...")
    descStr = """The program draws Spiropgraph using the Turtle Modules.
    When run with no arguments, this program draws random Spirographs.

    Terminology:

    R: radius of outer circle
    r: radius of inner circle
    l: ratio of hole distance to r


    """
    parse = argparse.ArgumentParser(description=descStr)

    parser.add_argument(
        "--sparam",
        nargs=3,
        dest="sparams",
        required=False,
        help="The three arguments in sparams: R, r, l.",
    )

    arg = parser.parse_args()

    turtle.setup(width=0.8)

    turtle.shape("turtle")

    turtle.title("Spirograph")

    turtle.onkey(saveDrawing, "s")

    turtle.listen()

    turtle.hideturtle()

    turtle.mainloop()


if __name__ == "__main__":
    main()
