from fasthtml.common import *
from datetime import datetime
import pathlib
import yaml

__all__ = ['blog_header', 'blog_post', "blog_footer", "tag", "tag_with_count", "markdown_page"]

def blog_header():
    return (
        Socials(site_name="Daniel Roy Greenfeld"),
        Header(
            A(Img(
                cls='borderCircle', alt='Daniel Roy Greenfeld', src='https://daniel.feldroy.com/_next/image?url=%2Fimages%2Fprofile.jpg&w=256&q=75', width='108', height='108')
                , href='/'),
            A(H2('Daniel Roy Greenfeld'), href="/"),
            P(
                A('About', href='/about'),'|', 
                A('Articles', href='/posts'), '|',
                A('Books', href='/books'), '|',
                A('Jobs', href='/jobs'), '|',
                A('Tags', href='/tags'), '|',
                A('Search', href='/search')
            ), style="text-align: center;"
        ))

def blog_post(title: str, slug: str, timestamp: str, description: str):
    return Span(
                H2(A(title, href=f"/posts/{slug}")),
                P(description, Small(Time(timestamp))),
        )

def blog_footer():
    return Footer(Hr(), P(
            A('Mastodon', href='https://fosstodon.org/@danielfeldroy'), '|',
            A('LinkedIn', href='https://www.linkedin.com/in/danielfeldroy/'), '|',
            A('Twitter', href='https://twitter.com/pydanny'), '|',
            A('Atom Feed', href='/feeds/atom.xml')
        ),
        P(f'All rights reserved {datetime.now().year}, Daniel Roy Greenfeld')
    )

def tag(slug: str):
    return A(slug, href=f"/tags/{slug}")

def tag_with_count(slug: str, count: int):
    return A(Span(slug), Small(f"({count})"), href=f"/tags/{slug}")

def markdown_page(slug: str):
    try:
        text = pathlib.Path(f"pages/{slug}.md").read_text()
    except FileNotFoundError:
        return Response("Page not found", status_code=404) 
    content = ''.join(text.split("---")[2:])
    metadata = yaml.safe_load(text.split("---")[1])
    return Title(metadata.get('Title', slug)), blog_header(), Main(
        A("← Back to home", href="/"),
        Section(
            Div(content,cls="marked")
        )
    ), blog_footer()