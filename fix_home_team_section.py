import io

path = "templates/sections/team.html"

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = "{{ member.bio|truncatewords:18 }}"
new = "{{ member.bio|striptags|truncatewords:18 }}"

if old in content:
    content = content.replace(old, new)

    with io.open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print("FIXED: added striptags filter before truncatewords.")
elif new in content:
    print("Already fixed - no changes needed.")
else:
    print("Could not find the expected line. Please check templates/sections/team.html manually.")
