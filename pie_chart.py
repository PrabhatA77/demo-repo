import matplotlib.pyplot as plt

# Sample data
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sizes = [30, 25, 20, 25]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0.05, 0, 0, 0)  # Explode 1st slice

# Create pie chart
plt.figure(figsize=(8,6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Fruit Distribution', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as circle

# Show the plot
plt.show()
