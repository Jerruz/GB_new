from re import compile

RFC5322 = r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
mail_check = compile(RFC5322)


def email_parse(email: str) -> dict:
    matched = mail_check.match(email)
    if matched is None:
        raise ValueError(f'wrong email: {email}')
    return {
        'username': matched[1],
        'domain': matched[2],
    }


if __name__ == '__main__':
    print(email_parse('test@test.com'))
    print(email_parse('test test.com'))
