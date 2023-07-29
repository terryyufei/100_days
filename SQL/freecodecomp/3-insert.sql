INSERT INTO office.employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO office.employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO office.branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO office.branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO office.branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO office.branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO office.branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO office.branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO office.branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO office.client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO office.client VALUES(401, 'Lackawana Country', 2);
INSERT INTO office.client VALUES(402, 'FedEx', 3);
INSERT INTO office.client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO office.client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO office.client VALUES(405, 'Times Newspaper', 3);
INSERT INTO office.client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO office.works_with VALUES(105, 400, 55000);
INSERT INTO office.works_with VALUES(102, 401, 267000);
INSERT INTO office.works_with VALUES(108, 402, 22500);
INSERT INTO office.works_with VALUES(107, 403, 5000);
INSERT INTO office.works_with VALUES(108, 403, 12000);
INSERT INTO office.works_with VALUES(105, 404, 33000);
INSERT INTO office.works_with VALUES(107, 405, 26000);
INSERT INTO office.works_with VALUES(102, 406, 15000);
INSERT INTO office.works_with VALUES(105, 406, 130000);
