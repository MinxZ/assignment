nn = 5;
ii = 12;
error_train_all = zeros(ii,1);
error_val_all = zeros(ii,1);
lambda = 0.01;
for n = 1:nn
   rand1 = randperm(12,ii);
   rand2 = randperm(21,ii);
   X_poly_r = X_poly(rand1,:);
   y_r = y(rand1,:);
   X_poly_val_r = X_poly_val(rand1,:);
   yval_r = yval(rand1,:);
   [error_train, error_val] = ...
    learningCurve(X_poly_r, y_r, X_poly_val_r, yval_r, lambda);
   error_train_all =bsxfun(@plus,error_train_all,error_train);
   error_val_all =bsxfun(@plus,error_val_all,error_val);
end
error_train = error_train_all./nn;
error_val = error_val_all./nn;

plot(1:m, error_train, 1:m, error_val);
title('Learning curve for linear regression')
legend('Train', 'Cross Validation')
xlabel('Number of training examples')
ylabel('Error')
axis([0 13 0 150])
