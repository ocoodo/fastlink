from pydantic import BaseModel, AnyHttpUrl


class NewLinkRequest(BaseModel):
    target: AnyHttpUrl
