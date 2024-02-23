# Attendance System using Convolutional Neural Networks

This project implements an Attendance System utilizing Convolutional Neural Networks (CNNs) in Python. The system is designed to automate attendance tracking for students. Below are the key features and details of the project:

## Overview

The Attendance System utilizes a CNN architecture with three main layers: Convolutional, Pooling, and Fully Connected Layer. It employs the Rectified Linear Unit (ReLU) activation function to enhance model performance.

## Key Features

- **CNN Architecture**: Utilized CNN architecture with Convolutional, Pooling, and Fully Connected layers.
- **Activation Function**: Implemented ReLU activation function for enhancing model performance.
- **Max Pooling**: Incorporated max pooling to increase robustness against variations in feature positions within input images.
- **Training**: Employed the Adam optimizer and trained the model for 250 epochs, achieving an impressive accuracy of 93.75%.
- **Performance Metrics**: Achieved a precision of 0.95 and F1 score of 0.94, indicative of high model performance and reliability.
- **Integration with Firebase**: Integrated Firebase for real-time database updates, facilitating seamless attendance tracking for students.

## Usage

To use the Attendance System:

1. Clone the repository from GitHub.
2. Install the necessary dependencies specified in the `requirements.txt` file.
3. Run the main script to initiate the attendance tracking process.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- TensorFlow
- Firebase SDK
- Other dependencies as specified in `requirements.txt`.

## Contributing

Contributions to improve the system are welcome. If you wish to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to all contributors and libraries used in this project.

---

Feel free to customize this README file according to your project's specific details and requirements.
