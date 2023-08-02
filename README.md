This Porject contains two files one for Feature file named EndPointResponseValidation.feature which contains Test Scenarios with Test Case written in Gherkin
Step Definition named "StepReqRes.py" contains the code definition for each step in the Feature file
Navigate to the "terminal" section on bottom of the Pycharm editor and run the below command
run "behave -f allure_behave.formatter:AllureFormatter -o reports/ features"
Now JSON format report will be generated to see html Allure Report
run this command "allure serve reports/" to see the reports in Graphical and Actual report of the test status
