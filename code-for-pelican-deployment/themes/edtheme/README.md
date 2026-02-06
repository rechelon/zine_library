## Configuration

### Basic Settings

```python
SITENAME = 'Your Blog Name'
SITESUBTITLE = 'A brief description of your blog'
SITEURL = 'https://yourblog.com'

# Logo (optional) - place in content/images/
SITELOGO = 'images/logo.png'  # Recommended: 200x200px

# Menu items
MENUITEMS = [
    ('Home', '/'),
    ('Archives', '/archives.html'),
]

# Display pages in menu
DISPLAY_PAGES_ON_MENU = True

# Social links (displayed in right sidebar)
SOCIAL = [
    ('Twitter', 'https://twitter.com/yourusername'),
    ('GitHub', 'https://github.com/yourusername'),
]

# External links (displayed in right sidebar)
LINKS = [
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://python.org/'),
]

# Tag cloud (displayed in right sidebar)
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 20
```

### Layout Customization

The theme uses CSS variables for easy customization. You can override these in a custom CSS file:

```css
:root {
    --color-ink: #1a1a1a;        /* Main text color */
    --color-paper: #fefdf8;      /* Background color */
    --color-accent: #c84630;     /* Accent/link color */
    --color-muted: #6b6b6b;      /* Secondary text */
    --color-border: #d4d4d4;     /* Borders */
    
    --sidebar-width: 280px;      /* Sidebar width on desktop */
    --header-height: 200px;      /* Header height */
    --max-width: 1400px;         /* Maximum content width */
}
```

## Template Structure

- `base.html` - Base template with header, footer, and three-column layout
- `index.html` - Homepage with article cards and pagination
- `article.html` - Individual blog post template
- `page.html` - Static page template
- `category.html` - Category archive template
- `tag.html` - Tag archive template
- `author.html` - Author archive template

## Sidebar Content

### Left Sidebar
- About section (uses SITESUBTITLE)
- Categories list

### Right Sidebar
- Tag cloud
- Social links (from SOCIAL setting)
- External links (from LINKS setting)

## Responsive Breakpoints

- **Desktop (>992px)**: Three-column layout with sticky sidebars
- **Tablet (768px-992px)**: Single column, sidebars stack below content
- **Mobile (<768px)**: Simplified single-column layout
- **Small Mobile (<480px)**: Further optimizations for small screens

## Customization Tips

1. **Custom Logo**: Add a 200x200px logo for best results
2. **Color Scheme**: Modify CSS variables to match your brand
3. **Fonts**: The theme uses Google Fonts (Playfair Display + Source Sans 3). You can replace these in the CSS.
4. **Layout Width**: Adjust `--max-width` and `--sidebar-width` variables


