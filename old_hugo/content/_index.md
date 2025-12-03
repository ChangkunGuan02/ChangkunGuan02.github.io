---
title: 'Home'
date: 2023-10-24
type: landing

# Note: `username` refers to the user's folder name in `content/authors/`

# Page sections
sections:
  - block: biography
    content:
      title: Biography
      username: admin
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
        icon_pack: fas
        icon: file-pdf
        color: indigo
        style: solid
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
      biography:
        # Customize the style of your biography text
        style: 'text-align: justify; font-size: 0.95em; line-height: 1.9; color: rgba(0, 0, 0, 0.85); padding: 1.5rem; background: rgba(248, 250, 252, 0.5); border-radius: 0.75rem;'
  
  - block: markdown
    content:
      title: Interests
      text: |
        * Optimization
        * Combinatorial Problems
        * Operations Research
        * Applied Mathematics
        * Statistical Analysis
  
  - block: experience
    content:
      title: Education
      username: admin
    design:
      spacing:
        padding: ['2rem', '0', '2rem', '0']
      # Hugo date format
      date_format: 'January 2006'
      # Education or Experience section first?
      is_education_first: true
 
  - block: collection
    id: research
    content:
      title: Research Projects
      filters:
        folders:
          - project
      count: 0
      offset: 0
      order: desc
      page_type: project
    design:
      spacing:
        padding: ['2rem', '0', '2rem', '0']
      view: card
      columns: '2'
  
  - block: markdown
    content:
      title: Contact
      text: |
        - **Email**: [changkunguan2333@gmail.com](mailto:changkunguan2333@gmail.com)
        - **GitHub**: [ChangkunGuan02](https://github.com/ChangkunGuan02)
        - **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/)
    design:
      spacing:
        padding: ['2rem', '0', '2rem', '0']
---
