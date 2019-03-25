%%% 1. Load Data %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Put Your Answer Code Here %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% movieList = 
% training =                
testing = readtable('testingSet.csv');


%%% 2. Convert to Sparse Matrix and Full Matrix %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Put Your Answer Code Here %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% sparse_UI =                       
% UI =     
% heatmap


%%% 3. Cosine Similarity Matrix for Users %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Put Your Answer Code Here %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
simU17 = UI(1,:)*UI(7,:)'/(norm(UI(1,:)) * norm(UI(7,:)));  %Example for similarity between user 1 and 7
% Suggested steps:
% 1. compute the row norm
% 2. use the formula to compute the similarity.. (tips: transform the UI)
% 3. change the diagonal elements to 0
% simU =


%%% 4. Estimate the rating user x gave to a list of unrated movie in the testing set %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Put Your Answer Code Here %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% x = 
toTest = testing(testing.userId == x,:);
% [simScore, neighbors] = 

% k =            % the top k neighbors
% estRating = simScore(1:k)*UI(neighbors(1:k),:)./sum(simScore(1:k));
% toTest.estRating = 


%%% 5. Evaluate the Estimation Using RMSE %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Put Your Answer Code Here %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% rmse = 
