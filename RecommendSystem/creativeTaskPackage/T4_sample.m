% load data =============================================================
movieList = readtable('movieList.csv', 'Format', '%u%q%q');  % get the list of movie
training = readtable('trainingSet.csv');
testing = readtable('testingSet.csv');

% create a user item matrix, from training dataset =======================
sUI = sparse(training.userId, training.movieId, training.rating);
UI = full(sUI);

% compute the cosine similarity ==========================================
norm_x = vecnorm(UI,2,1);   %sum(UI.^2).^(1/2);
norm_y = vecnorm(UI,2,2)';   %sum(UI'.^2).^(1/2);
simU = UI*UI'./(norm_y'*norm_y);    % user-based similarity
simU(find(eye(size(simU,1)))) = 0;
simI = UI'*UI./(norm_x'*norm_x);    % item-based similarity
simI(find(eye(size(simI,1)))) = 0; 

% for all users in the testing dataset ===================================
usersToTest = unique(testing.userId); 
[simScore, neighbors] = sort(simU(usersToTest,:), 2, 'descend');
k = 3;

% according to the slide 5 - user-based approach =========================
testing.estRating = zeros(height(testing),1);
for i=1:length(usersToTest)
    estRating = simScore(i, 1:k)*UI(neighbors(i,1:k),:)./sum(simScore(i,1:k));
    
    ind = testing.userId == usersToTest(i);
    testing.estRating(ind) = estRating(testing.movieId(ind))';
end

% evaluate your result ===================================================
benchmarkT4(testing, 'James She', '123456');




    