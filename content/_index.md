---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: stats
    content:
      items:
        - statistic: "50+"
          description: |
            Publications
        - statistic: "770+"
          description: |
            Citations
        - statistic: "14"
          description: |
            h-index
    design:
      # Section background color (CSS class)
      css_class: "bg-gray-100 dark:bg-gray-900"
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
  - block: markdown
    content:
      title: '📚 My Research'
      subtitle: ''
      text: |-
        I am a research scientist specializing in deep learning applications for cybersecurity and smart agriculture. My work focuses on designing efficient, lightweight, and real-time AI models for UAV-based plant disease detection, intrusion detection systems, and cyber-attack prevention.

        Through a series of recent publications - including EF-CenterNet, MobileH-Transformer, TinyResViT, DetectVul, and XSShield - I aim to bridge the gap between cutting-edge AI models and practical deployment in resource-constrained environments such as IoT and edge devices.

        I leverage both quantitative and qualitative approaches to explore how artificial intelligence can enhance sustainability, security, and performance in real-world systems. I’m always open to collaboration—feel free to connect!
    design:
      columns: 1
  - block: collection
    id: papers
    content:
      title: Recent Publications
      filters:
        folders:
          - publication
        featured_only: true
      count: 6
    design:
      view: article-grid
      columns: 2
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     view: article-grid
  #     columns: 1

  # - block: collection
  #   id: news
  #   content:
  #     title: Recent News
  #     subtitle: ''
  #     text: ''
  #     # Page type to display. E.g. post, talk, publication...
  #     page_type: post
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 6
  #     # Filter on criteria
  #     filters:
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     # Choose how many pages you would like to offset by
  #     offset: 0
  #     # Page order: descending (desc) or ascending (asc) date.
  #     order: desc
  #   design:
  #     # Choose a layout view
  #     view: date-title-summary
  #     # Reduce spacing
  #     spacing:
  #       padding: [0, 0, 0, 0]
---
