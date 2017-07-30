import requests
try: 
    import BeautifulSoup #python2
    version = 2
except ImportError:
    import bs4 as BeautifulSoup #python3
    version = 3

def get_people(query, options="general", recurse=False):
    """Accesses the MIT People Directory

    Args:
        query (str): The name, email, or phone number to search for
        options (str, optional): The type of search to do. Should be one of
            "general" -- name/email
            "phone" -- reverse lookup (10 digits)
            "lastnamesx" -- lastname sounds like
        recurse (bool, optional): Whether or not additional requests should
            be made to retrieve all fields when multiple results are found.
            Defaults to False.
    
    Returns:
        list: The people found.
            Each element is a dictionary containing the person's details.
            The dictionary will at least contain a "name" field.

    """

    url = "http://web.mit.edu/bin/cgicso?options="+options+"&query="+query
    response = requests.get(url)
    html = response.content

    if version == 2:
        soup = BeautifulSoup.BeautifulSoup(html)
    if version == 3:
        soup = BeautifulSoup.BeautifulSoup(html, "html.parser")
    payload = soup.find("pre")

    output = []

    # case 1: no matches
    if "No matches to your query." in payload.text:
        return output

    # case 2: multiple matches
    if isinstance(payload.contents[0], BeautifulSoup.Tag):
        if payload.contents[0].name == "a":
            for a in payload.findAll("a", href=True):
                if recurse:
                    raise NotImplementedError #TODO
                else:
                    output.append({"name": a.contents[0]})
            return output

    # case 3: one match
    user_dict = {}
    for content in payload.contents:
        if isinstance(content, BeautifulSoup.Tag):
            user_dict[u"email"] = content.contents[0]
        else:
            for field_val in map(lambda s: s.strip(), content.split("\n")):
                if not (field_val == "" or field_val.startswith("email:")):
                    field, val = field_val.split(': ', 1)
                    user_dict[field] = val.strip()
    output.append(user_dict)
    return output
