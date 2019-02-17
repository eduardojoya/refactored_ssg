#template files
top_template = open('templates/top.html').read()
bottom_template = open('templates/bottom.html').read()

#Read in Index HTML code
content = open('content/index.html').read()

#Combine with content index HTML code
index_html = top_template + content + bottom_template
open('docs/index.html', 'w+').write(index_html)

#Combine with content resume HTML code
content = open('content/resume.html').read()
resume_html = top_template + content + bottom_template
open('docs/resume.html', 'w+').write(resume_html)

#Combine with content education HTML code
content = open('content/education.html').read()
education_html = top_template + content + bottom_template
open('docs/education.html', 'w+').write(education_html)

#Combine with interests HTML code
content = open('content/interests.html').read()
interests_html = top_template + content + bottom_template
open('docs/interests.html', 'w+').write(interests_html)

#Combine with blog HTML code
content = open('content/blog.html').read()
blog_html = top_template + content + bottom_template
open('docs/content.html', 'w+').write(blog_html)
