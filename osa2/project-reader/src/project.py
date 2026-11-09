class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n - ".join(dependencies) if len(dependencies) > 0 else "-"

    def _stringify_authors(self, authors):
        names = []
        for author in authors:
            name = author.get('name')
            names.append(f" - {name}")
        return "\n".join(names)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: \n{self._stringify_authors(self.authors)}"
            f"\nDependencies: \n - {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: \n - {self._stringify_dependencies(self.dev_dependencies)}"
        )
