class Search:

    def by_language(

        self,

        snippets,

        language

    ):

        return [

            s

            for s in snippets

            if s.language.lower()

            == language.lower()

        ]

    def by_tag(

        self,

        snippets,

        tag

    ):

        return [

            s

            for s in snippets

            if tag.lower()

            in [

                t.lower()

                for t in s.tags

            ]

        ]
