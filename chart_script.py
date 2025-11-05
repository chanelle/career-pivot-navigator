import plotly.graph_objects as go
import plotly.express as px

# Create a comprehensive network diagram for Career Pivot Navigator architecture
# Define node positions with better spacing for clarity
nodes = {
    # User Input Layer (Left) - 6 inputs vertically spaced
    'Current Role': (0, 6),
    'Skills': (0, 5),
    'Pain Points': (0, 4),
    'Interests': (0, 3),
    'Constraints': (0, 2),
    'Budget/Time': (0, 1),
    
    # Processing Layer (Center-Left) - Better vertical spacing
    'Input Normalize\n(utils.py)': (3, 4.5),
    'Career Analyzer\n(LangChain)': (6, 5.5),
    'Career Analysis\n(1-2 recs)': (9, 5),
    'Plan Generator\n(LangChain)': (12, 4),
    
    # Database Layer (Center) - 3 components with career details
    'Career Map DB\n(8 careers)': (6, 2.5),
    'Skill Mappings\n(12+ skills)': (6, 1.5),
    'Pain Solutions\n(7 pain pts)': (6, 0.5),
    
    # Output Layer (Center-Right) - 4 outputs vertically spaced
    '3-Step Plan': (15, 5.5),
    'Monetization\nStrategy': (15, 4.5),
    'Resume\nReframe': (15, 3.5),
    'Mindset\nCoaching': (15, 2.5),
    
    # Export Layer (Right) - 4 export options
    'Export\nMarkdown': (18, 5),
    'Export\nJSON': (18, 4),
    'Export\nNotion': (18, 3),
    'Export\nPDF': (18, 2)
}

# Define connections showing data flow
edges = [
    # All inputs to normalization
    ('Current Role', 'Input Normalize\n(utils.py)'),
    ('Skills', 'Input Normalize\n(utils.py)'),
    ('Pain Points', 'Input Normalize\n(utils.py)'),
    ('Interests', 'Input Normalize\n(utils.py)'),
    ('Constraints', 'Input Normalize\n(utils.py)'),
    ('Budget/Time', 'Input Normalize\n(utils.py)'),
    
    # Processing pipeline
    ('Input Normalize\n(utils.py)', 'Career Analyzer\n(LangChain)'),
    ('Career Analyzer\n(LangChain)', 'Career Analysis\n(1-2 recs)'),
    ('Career Analysis\n(1-2 recs)', 'Plan Generator\n(LangChain)'),
    
    # Database to analyzer
    ('Career Map DB\n(8 careers)', 'Career Analyzer\n(LangChain)'),
    ('Skill Mappings\n(12+ skills)', 'Career Analyzer\n(LangChain)'),
    ('Pain Solutions\n(7 pain pts)', 'Career Analyzer\n(LangChain)'),
    
    # Plan generator to outputs
    ('Plan Generator\n(LangChain)', '3-Step Plan'),
    ('Plan Generator\n(LangChain)', 'Monetization\nStrategy'),
    ('Plan Generator\n(LangChain)', 'Resume\nReframe'),
    ('Plan Generator\n(LangChain)', 'Mindset\nCoaching'),
    
    # All outputs to all exports
    ('3-Step Plan', 'Export\nMarkdown'),
    ('3-Step Plan', 'Export\nJSON'),
    ('3-Step Plan', 'Export\nNotion'),
    ('3-Step Plan', 'Export\nPDF'),
    ('Monetization\nStrategy', 'Export\nMarkdown'),
    ('Monetization\nStrategy', 'Export\nJSON'),
    ('Monetization\nStrategy', 'Export\nNotion'),
    ('Monetization\nStrategy', 'Export\nPDF'),
    ('Resume\nReframe', 'Export\nMarkdown'),
    ('Resume\nReframe', 'Export\nJSON'),
    ('Resume\nReframe', 'Export\nNotion'),
    ('Resume\nReframe', 'Export\nPDF'),
    ('Mindset\nCoaching', 'Export\nMarkdown'),
    ('Mindset\nCoaching', 'Export\nJSON'),
    ('Mindset\nCoaching', 'Export\nNotion'),
    ('Mindset\nCoaching', 'Export\nPDF'),
]

# Define node colors by category
node_colors = {
    # Input nodes - Strong cyan
    'Current Role': '#1FB8CD', 'Skills': '#1FB8CD', 'Pain Points': '#1FB8CD',
    'Interests': '#1FB8CD', 'Constraints': '#1FB8CD', 'Budget/Time': '#1FB8CD',
    
    # Processing nodes - Bright red
    'Input Normalize\n(utils.py)': '#DB4545', 'Career Analyzer\n(LangChain)': '#DB4545',
    'Career Analysis\n(1-2 recs)': '#DB4545', 'Plan Generator\n(LangChain)': '#DB4545',
    
    # Database nodes - Sea green
    'Career Map DB\n(8 careers)': '#2E8B57', 'Skill Mappings\n(12+ skills)': '#2E8B57', 
    'Pain Solutions\n(7 pain pts)': '#2E8B57',
    
    # Output nodes - Cyan
    '3-Step Plan': '#5D878F', 'Monetization\nStrategy': '#5D878F',
    'Resume\nReframe': '#5D878F', 'Mindset\nCoaching': '#5D878F',
    
    # Export nodes - Moderate yellow
    'Export\nMarkdown': '#D2BA4C', 'Export\nJSON': '#D2BA4C',
    'Export\nNotion': '#D2BA4C', 'Export\nPDF': '#D2BA4C'
}

# Create the figure
fig = go.Figure()

# Add edges with better styling
edge_x = []
edge_y = []
for edge in edges:
    x0, y0 = nodes[edge[0]]
    x1, y1 = nodes[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

fig.add_trace(go.Scatter(x=edge_x, y=edge_y,
                         line=dict(width=1.5, color='#666666'),
                         hoverinfo='none',
                         mode='lines',
                         showlegend=False))

# Add nodes with improved sizing and text
for node, (x, y) in nodes.items():
    fig.add_trace(go.Scatter(x=[x], y=[y],
                            mode='markers+text',
                            marker=dict(size=35,
                                      color=node_colors[node],
                                      line=dict(width=2, color='white')),
                            text=node,
                            textposition="middle center",
                            textfont=dict(size=9, color='white', family='Arial Black'),
                            hovertemplate=f'<b>{node}</b><extra></extra>',
                            showlegend=False))

# Add section background rectangles for better grouping
fig.add_shape(type="rect", x0=-1, y0=0.5, x1=1, y1=6.5,
              line=dict(color="#1FB8CD", width=2), fillcolor="rgba(31, 184, 205, 0.1)")

fig.add_shape(type="rect", x0=2, y0=3.5, x1=13, y1=6,
              line=dict(color="#DB4545", width=2), fillcolor="rgba(219, 69, 69, 0.1)")

fig.add_shape(type="rect", x0=5, y0=0, x1=7, y1=3,
              line=dict(color="#2E8B57", width=2), fillcolor="rgba(46, 139, 87, 0.1)")

fig.add_shape(type="rect", x0=14, y0=2, x1=16, y1=6,
              line=dict(color="#5D878F", width=2), fillcolor="rgba(93, 135, 143, 0.1)")

fig.add_shape(type="rect", x0=17, y0=1.5, x1=19, y1=5.5,
              line=dict(color="#D2BA4C", width=2), fillcolor="rgba(210, 186, 76, 0.1)")

# Add section labels
fig.add_annotation(x=0, y=7, text="<b>👤 USER INPUT</b>", showarrow=False,
                   font=dict(size=12, color='#1FB8CD', family='Arial Black'))

fig.add_annotation(x=7.5, y=6.5, text="<b>⚙️ PROCESSING LAYER</b>", showarrow=False,
                   font=dict(size=12, color='#DB4545', family='Arial Black'))

fig.add_annotation(x=6, y=-0.5, text="<b>🗄️ CAREER DATABASE</b>", showarrow=False,
                   font=dict(size=12, color='#2E8B57', family='Arial Black'))

fig.add_annotation(x=15, y=6.5, text="<b>📋 OUTPUT GENERATION</b>", showarrow=False,
                   font=dict(size=12, color='#5D878F', family='Arial Black'))

fig.add_annotation(x=18, y=6, text="<b>📤 EXPORT OPTIONS</b>", showarrow=False,
                   font=dict(size=12, color='#D2BA4C', family='Arial Black'))

# Add legend
legend_y_start = -2
legend_items = [
    ("User Input", "#1FB8CD"),
    ("Processing", "#DB4545"), 
    ("Database", "#2E8B57"),
    ("Outputs", "#5D878F"),
    ("Export", "#D2BA4C")
]

for i, (label, color) in enumerate(legend_items):
    fig.add_trace(go.Scatter(x=[i*3], y=[legend_y_start],
                            mode='markers+text',
                            marker=dict(size=20, color=color),
                            text=label,
                            textposition="bottom center",
                            textfont=dict(size=10, color='black'),
                            showlegend=False,
                            hoverinfo='skip'))

# Update layout
fig.update_layout(
    title="Career Pivot Navigator Architecture & Data Flow",
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-2, 20]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3, 8]),
    plot_bgcolor='white',
    hovermode='closest'
)

# Save the chart
fig.write_image('career_pivot_architecture.png')
fig.write_image('career_pivot_architecture.svg', format='svg')

print("Improved Career Pivot Navigator architecture chart created successfully!")