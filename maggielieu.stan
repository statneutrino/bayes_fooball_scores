//
// This Stan program defines a simple model, with a
// vector of values 'y' modeled as normally distributed
// with mean 'mu' and standard deviation 'sigma'.
//
// Learn more about model development with Stan at:
//
//    http://mc-stan.org/users/interfaces/rstan.html
//    https://github.com/stan-dev/rstan/wiki/RStan-Getting-Started
//

// The input data is a vector 'y' of length 'N'.
data {
  int<lower=0> nt; //number of teams
  int<lower=0> ng; //number of games
  int<lower=0> ht[ng]; //home team index
  int<lower=0> at[ng]; //away team index
  int<lower=0> s1[ng]; //score home team
  int<lower=0> s2[ng]; //score away team
  //int<lower=0> np; //number of predicted games
  //int<lower=0> htnew[np]; //home team index for prediction
  //int<lower=0> atnew[np]; //away team index for prediction
}

parameters {
  real home; //home advantage
  vector[nt] att; //attack ability of each team
  vector[nt] def; //defence ability of each team
  //hyper parameters
  real mu_att;
  real<lower=0> tau_att;
  real mu_def;
  real<lower=0> tau_def;
}

transformed parameters {
  vector[ng] theta1; //score probability of home team
  vector[ng] theta2; //score probability of away team

  theta1 = exp(home + att[ht] - def[at]);
  theta2 = exp(att[at] - def[ht]);

}

model {
//hyper priors
mu_att ~ normal(0,0.1);
tau_att ~ normal(0,1);
mu_def ~ normal(0,0.1);
tau_def ~ normal(0,1);

//priors
att ~ normal(mu_att, tau_att);
def ~ normal(mu_def, tau_def);
home ~ normal(0,0.0001);


//likelihood
    s1 ~ poisson(theta1);
    s2 ~ poisson(theta2);
}

generated quantities {
//generate predictions
  //vector[np] theta1new; //score probability of home team
  //vector[np] theta2new; //score probability of away team
  //real s1new[np]; //predicted score
  //real s2new[np]; //predicted score


  //theta1new = exp(home + att[htnew] - def[atnew]);
  //theta2new = exp(att[atnew] - def[htnew]);

  //s1new = poisson_rng(theta1new);
  //s2new = poisson_rng(theta2new);
}

