pages = [    
        {   'filename': 'content/index.html',
            'output': 'docs/index.html',
            'title': 'About Me',   
        },
        {
            'filename': 'content/resume.html',
            'output': 'docs/resume.html',
            'title': 'Resume',
        },
        {
            'filename': 'content/education.html',
            'output': 'docs/education.html',
            'title': 'Education',
        },
        {
            'filename': 'content/interests.html',
            'output': 'docs/interests.html',
            'title': 'Interests',
        },
        {  
            'filename': 'content/blog.html',
            'output': 'docs/blog.html',
            'title': 'Coding Journey Blog',
        },
       ]


def apply_template(template, page_title, file_name): 
    index_content = open(file_name).read()  
    finished_index_page = template.replace('{{content}}', index_content) 
    finished_index_page = finished_index_page.replace('{{title}}', page_title)  
    return finished_index_page 

def output_page(template,page):
    file_name = page['filename']
    page_output = page['output']
    page_title = page['title']
    
    output_html = apply_template(template, page_title, file_name)
    open(page_output, 'w+').write(output_html)

def main():
    template = open('templates/base.html').read() 
    for page in pages:    
        output_page(template, page)

if __name__ == "__main__": 
    main()
