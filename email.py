def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
    return new_email


print(replace_domain("ashikcuet17spsc15@programmer.net", "programmer,net", "gamil.com"))
