import Evaluation.Evaluation as Eval

# Input directory of model
model_dir = input("Please input the directory of the trained model:")

model_prefix = "\\" + input("Please input the prefix of the trained model.\n"
                            "e.g. YYYY-MM-DD_nameOfModel:")

# Input directory to save evaluation results
save_dir = input("Please input the directory to save generated figures:")

# Instantiate object
fitted_model = Eval.FittedModel(model_dir, model_prefix, save_dir)

fitted_model.save_acc_fig()
fitted_model.save_loss_fig()
fitted_model.save_arch_fig()
fitted_model.predict_image()
