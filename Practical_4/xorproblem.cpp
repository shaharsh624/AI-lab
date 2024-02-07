#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Function to calculate the step function
int stepFunction(double z)
{
    return (z >= 0) ? 1 : 0;
}

// Function to train the perceptron
void trainPerceptron(vector<vector<int>> &X, vector<int> &y, vector<double> &weights, double alpha, int epochs)
{
    int n = weights.size() - 1;
    int m = X.size();

    for (int epoch = 0; epoch < epochs; ++epoch)
    {
        for (int i = 0; i < m; ++i)
        {
            double z = weights[0];

            for (int j = 0; j < n; ++j)
            {
                z += weights[j + 1] * X[i][j];
            }

            int prediction = stepFunction(z);

            weights[0] += alpha * (y[i] - prediction);

            for (int j = 0; j < n; ++j)
            {
                weights[j + 1] += alpha * (y[i] - prediction) * X[i][j];
            }
        }
    }
}

int main()
{
    vector<vector<int>> X = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    vector<int> y = {0, 1, 1, 0};

    vector<double> weights = {0.5, -0.5, 0.5};
    double alpha = 0.1;
    int epochs = 100;

    trainPerceptron(X, y, weights, alpha, epochs);

    cout << "Learned Weights: ";
    for (double w : weights)
    {
        cout << w << " ";
    }
    cout << endl;

    return 0;
}
