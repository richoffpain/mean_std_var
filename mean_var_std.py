import numpy as np


"""
_ rreceive a list as input
 _len should be 9 or higher
 _ transform list into a 3x3 matrix

_ calculate 
 _ mean. max. min. standard deviation

_ return a dict of list 
"""

def calculate(list):
    calculations = dict()

    if len(list) < 9:
        raise ValueError ("List must contain nine numbers.")
    else:
        # convert the liist into a numpy array and trasform to a 3x3 matrix
        data = np.array(list)
        data_matrix = data.reshape(3,3)
        #print(data_matrix)
        # calculate Mean
        total_mean = np.mean(data_matrix)
        rows_mean = np.mean(data_matrix, axis=1)
        cols_mean = np.mean(data_matrix, axis=0)
        mean = [cols_mean.tolist(), rows_mean.tolist(), total_mean.tolist()]
        #print(mean)

        # calculate variance
        total_variance = np.var(data_matrix)
        rows_var = np.var(data_matrix, axis=1)
        cols_var = np.var(data_matrix, axis=0)
        var = [cols_var.tolist(), rows_var.tolist(), total_variance.tolist()]
        

        # calculate standard deviation
        total_std = np.std(data_matrix)
        rows_std = np.std(data_matrix, axis=1)
        cols_std = np.std(data_matrix, axis=0)
        std = [cols_std.tolist(), rows_std.tolist(), total_std.tolist()]

        # calculate the max
        total_max = np.max(data_matrix)
        rows_max = np.max(data_matrix, axis=1)
        cols_max = np.max(data_matrix, axis=0)
        maxi = [cols_max.tolist(), rows_max.tolist(), total_max.tolist()]

        # calculate the min
        total_min = np.min(data_matrix)
        rows_min = np.min(data_matrix, axis=1)
        cols_min = np.min(data_matrix, axis=0)
        mini = [cols_min.tolist(), rows_min.tolist(), total_min.tolist()]

        # calculate the sum 
        total_sum = np.sum(data_matrix)
        rows_sum = np.sum(data_matrix, axis=1)
        cols_sum = np.sum(data_matrix, axis=0)
        sumi = [cols_sum.tolist(), rows_sum.tolist(), total_sum.tolist()]




    # return {"mean": [row_means.tolist(), col_means.tolist(), total_mean]}
    # return the calculation dict of list
    calculations = {"mean": mean,
                    "variance": var,
                    "standard deviation": std,
                    "max": maxi, 
                    "min": mini,
                    "sum": sumi}
    return calculations


    
if __name__ == '__main__':
    main()