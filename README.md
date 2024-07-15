## **Flask Application Design to Build a Travel Education Website**

## **HTML Files**

- **index.html**: The homepage of the website. It will contain introductory information about the website and its purpose, along with links to various travel education resources.
- **destinations.html**: Will display a list of travel destinations, each with its own page.
- **destination_details.html**: Will provide detailed information about a specific travel destination, including its history, culture, landmarks, and travel tips.
- **resources.html**: Will offer a collection of travel resources, such as articles, videos, and other helpful materials on travel planning, budgeting, and safety.
- **contact.html**: Will include contact information and a form for users to reach out to the website's creators.

## **Routes**

- **@app.route('/')**: The homepage route that displays index.html.
- **@app.route('/destinations')**: The destinations route that displays destinations.html.
- **@app.route('/destination/<destination_id>')**: The destination details route that displays destination_details.html for the specified destination.
- **@app.route('/resources')**: The resources route that displays resources.html.
- **@app.route('/contact')**: The contact route that displays contact.html.