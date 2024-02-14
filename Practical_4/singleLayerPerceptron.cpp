#include <bits/stdc++.h>
using namespace std;

pair<int, int> input_dimensions = {8, 2};

vector<pair<double, double>> X = {{0.32, 0.41}, {0.27, 0.54}, {0.57, 0.42}, {0.59, 0.71}, {0.78, 0.82}, {0.79, 0.95}, {1.0, 0.85}, {1.0, 1.1}};

vector<double> coefficients, results, hidden_values, bias;
vector<double> targets = {0, 1, 0, 1, 0, 1, 0, 1};

void initialize_coefficients()
{
    uniform_real_distribution<double> unif(-0.00002, 0.00002);
    default_random_engine re;

    for (int i = 0; i < input_dimensions.second; i++)
    {
        coefficients.push_back(unif(re));
    }

    bias.push_back(unif(re));
}

void calculate_hidden_values()
{
    double res1, sum;
    sum = 0;
    hidden_values.clear();

    for (int i = 0; i < input_dimensions.first; i++)
    {
        res1 = (X[i].first) * (coefficients[0]) + (X[i].second) * (coefficients[1]);
        hidden_values.push_back((res1 + bias[0]));
    }
}

void make_predictions()
{
    calculate_hidden_values();
    results.clear();

    for (int i = 0; i < input_dimensions.first; i++)
    {
        if (hidden_values[i] > 0)
        {
            results.push_back(1);
        }
        else
        {
            results.push_back(0);
        }
    }
}

double evaluate_accuracy()
{
    double acc = 0;
    for (int i = 0; i < input_dimensions.first; i++)
    {
        if (results[i] == targets[i])
        {
            acc++;
        }
    }
    return acc / input_dimensions.first;
}

void adjust_coefficients(double learning_rate)
{
    double error1, error2;
    error1 = 0;
    error2 = 0;

    for (int i = 0; i < input_dimensions.first; i++)
    {
        error1 += (targets[i] - results[i]) * X[i].first;
        error2 += (targets[i] - results[i]) * X[i].second;

        bias[0] += learning_rate * (targets[i] - results[i]);
    }

    coefficients[0] += learning_rate * error1;
    coefficients[1] += learning_rate * error2;
}

int main()
{
    double learning_rate, accuracy;
    learning_rate = 0.000000001;

    initialize_coefficients();
    make_predictions();
    accuracy = evaluate_accuracy();

    long long ep = 1;
    while (accuracy < 1)
    {
        adjust_coefficients(learning_rate);
        make_predictions();
        accuracy = evaluate_accuracy();
        // cout << "\tepoch: " << ep << "\taccuracy: " << accuracy << "\n";
        ep++;
    }

    cout << "Weights: " << coefficients[0] << ", " << coefficients[1] << endl;

    return 0;
}
