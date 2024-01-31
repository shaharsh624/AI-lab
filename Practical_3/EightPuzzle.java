import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class EightPuzzle {

    static List<int[][]> visited = new ArrayList<>();
    static List<int[][]> open = new ArrayList<>();
    static List<int[][]> closed = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] startMatrix = getMatrixInput(scanner, "Enter the start matrix:");
        int[][] endMatrix = getMatrixInput(scanner, "Enter the end matrix:");

        closed.add(startMatrix);

        aStar8Puzzle(startMatrix, endMatrix);
    }

    static int[][] getMatrixInput(Scanner scanner, String prompt) {
        System.out.println(prompt);
        int[][] matrix = new int[3][3];
        for (int i = 0; i < 3; i++) {
            System.out.print("Enter row " + (i + 1) + " (separate numbers with space): ");
            String[] input = scanner.nextLine().split(" ");
            for (int j = 0; j < 3; j++) {
                matrix[i][j] = Integer.parseInt(input[j]);
            }
        }
        return matrix;
    }

    static int heuristic(int[][] matrix, int[][] endMatrix) {
        int count = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] != endMatrix[i][j] && matrix[i][j] != 0) {
                    count++;
                }
            }
        }
        return 9 - count;
    }

    static List<int[][]> possibleChildren(int[][] matrix, int[][] endMatrix) {
        int[][] direction = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
        int[][] newMatrix;
        int[][] temp;

        int row = -1, col = -1;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    row = i;
                    col = j;
                    break;
                }
            }
        }

        List<int[][]> children = new ArrayList<>();
        for (int[] dir : direction) {
            int ni = row + dir[0];
            int nj = col + dir[1];
            if (ni >= 0 && ni < 3 && nj >= 0 && nj < 3) {
                newMatrix = Arrays.stream(matrix).map(int[]::clone).toArray(int[][]::new);
                temp = Arrays.stream(matrix).map(int[]::clone).toArray(int[][]::new);
                newMatrix[row][col] = matrix[ni][nj];
                newMatrix[ni][nj] = 0;

                boolean found = false;
                for (int[][] vis : visited) {
                    if (Arrays.deepEquals(vis, newMatrix)) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    visited.add(newMatrix);
                    children.add(newMatrix);
                }
            }
        }
        return children;
    }

    static boolean aStar8Puzzle(int[][] startMatrix, int[][] endMatrix) {
        int startHeuristic = heuristic(startMatrix, endMatrix);
        if (startHeuristic == 0) {
            for (int[][] node : closed) {
                printMatrix(node);
            }
            return true;
        } else {
            List<int[][]> children = possibleChildren(startMatrix, endMatrix);
            if (!children.isEmpty()) {
                open.addAll(children);
            }

            while (!open.isEmpty()) {
                int[][] newMatrix = open.get(0);
                int newHeuristic = heuristic(newMatrix, endMatrix);
                closed.add(newMatrix);
                open.remove(0);

                if (newHeuristic == 0) {
                    for (int[][] node : closed) {
                        printMatrix(node);
                    }
                    return true;
                } else {
                    if (aStar8Puzzle(newMatrix, endMatrix)) {
                        return true;
                    }
                }
            }
            return false;
        }
    }

    static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
