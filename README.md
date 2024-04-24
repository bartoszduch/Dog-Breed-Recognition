<h1>Dog Breed Recognition using Web Scraping and Deep Learning</h1>

<p>This project aims to build a deep learning model that can recognize basic dog breeds. The model is trained using images collected from the internet using web scraping techniques. The collected images are then divided into training and testing sets to train and evaluate the model's performance.</p>

<h2>Web Scraping</h2>

<p>I use web scraping to collect images of various dog breeds from the internet. The <code>download_images_from_page</code> function downloads images from a specified webpage containing dog images. It saves the images to a specified directory on the local machine.</p>

<h2>Data Organization</h2>

<p>The downloaded images are stored in two separate directories:</p>
<ul>
  <li><strong>training_data:</strong> Contains images used for training the model.</li>
  <li><strong>testing_data:</strong> Contains images used for evaluating the model.</li>
</ul>

<h2>Model Training</h2>

<p>I use a Convolutional Neural Network architecture implemented in TensorFlow/Keras to train the model. The <code>load_data_from_directory</code> function loads the image data from the specified directories, preprocesses them, and prepares them for training. The CNN model is trained on the training data using the <code>fit</code> method.</p>

<h2>Model Evaluation</h2>

<p>After training the model, we evaluate its performance using the testing data. The <code>evaluate</code> method is used to calculate the loss and accuracy of the model on the testing data.</p>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>TensorFlow</li>
  <li>Keras</li>
  <li>requests</li>
  <li>BeautifulSoup</li>
</ul>
