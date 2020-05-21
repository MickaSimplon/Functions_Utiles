def linearRegression (X,y) : 
    ## Split data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    ## entrainemennt model
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    ### Prediction sur l'ensemble du test
    y_pred = regressor.predict(X_test)
    coef= regressor.coef_
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    adj_r2 =1-(1-r2)*(X_test.shape[0]-1)/(X_test.shape[0]-X_test.shape[1]-1)
    print('Coefficients : ',regressor.coef_)
    print('MAE : ',mae)
    print('MSE : ',mse)
    print('R² : ',r2)
    print('Adjusted R² : ',adj_r2)
    # un petit graph ca fait toujours plaisir
    to_plot = pd.DataFrame([[y_test.values[i], y_pred[i]] for i in range(len(y_test))], columns=['test', 'pred']).sort_values('test')
    plt.scatter(np.arange(len(y_test)), to_plot['test'], c='red')
    plt.plot(np.arange(len(y_test)), to_plot['pred'])
    return [mae,mse,rmse,r2,adj_r2]