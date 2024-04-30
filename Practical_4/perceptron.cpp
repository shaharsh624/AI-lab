#include <iostream>
#include <vector>

using namespace std;

vector<double> weights;
double learningRate;
double b = 0;

// Dot product function
double dotProduct(const vector<double> &v1, const vector<double> &v2)
{
    double sum = 0.0;
    for (int i = 0; i < v1.size(); ++i)
    {
        sum += (v1[i] * v2[i]) + b;
    }
    return sum;
}

// Train the perceptron on a single data point
void train(const vector<double> &input, int label)
{
    double output = dotProduct(input, weights);
    int predictedLabel = (output >= 0) ? 1 : 0;

    if (predictedLabel != label)
    {
        for (int i = 0; i < weights.size(); ++i)
        {
            weights[i] += learningRate * (label - predictedLabel) * input[i];
            b += learningRate * (label - predictedLabel);
        }
    }
}

int main()
{
    vector<vector<double>> inputs = {
        {0.25, 0.353}, {0.25, 0.471}, {0.5, 0.353}, {0.5, 0.647}, {0.75, 0.705}, {0.75, 0.882}, {1, 0.705}, {1, 1}};
    vector<int> labels = {0, 1, 0, 1, 0, 1, 0, 1};

    learningRate = 0.1;
    weights = vector<double>(inputs[0].size(), 0.0);

    // Train the perceptron
    int numEpochs = 50;
    for (int epoch = 0; epoch < numEpochs; ++epoch)
    {
        for (int i = 0; i < inputs.size(); ++i)
        {
            train(inputs[i], labels[i]);
        }
    }

    cout << "Learned weights: ";
    for (double weight : weights)
    {
        cout << weight << " ";
    }
    cout << endl;
    cout << "Learned Bias: " << b << endl;

    return 0;
}