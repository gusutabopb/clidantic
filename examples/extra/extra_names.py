from pydantic import BaseModel, Field

from clidantic import Parser

cli = Parser()


class Config(BaseModel):
    name: str = Field(cli={"names": ("-n", "--old-name")})
    count: int = Field(cli={"names": ("-c",)})


@cli.command()
def hello(args: Config):
    print(args)


if __name__ == "__main__":
    cli()
