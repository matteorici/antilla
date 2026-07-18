from tags import format_tags


def show(snippets):

    print()

    print("Code Snippets")

    print()

    for snippet in snippets:

        print(

            snippet.language

        )

        print()

        print(

            snippet.title

        )

        print()

        print("Tags:")

        print(

            format_tags(

                snippet.tags

            )

        )

        print()

        print(

            "-" * 25

        )

        print()
