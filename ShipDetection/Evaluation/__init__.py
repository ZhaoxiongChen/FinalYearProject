import time
import Evaluation.Evaluation as Eval


date = time.strftime("%Y-%m-%d_%H%M", time.localtime())
model_dir = input("Please input the directory of the trained model:")
save_dir = input("Please input the directory of generated figures:")


fitted_model = Eval.FittedModel(model_dir, date, save_dir)
fitted_model.save_acc_fig()
fitted_model.save_loss_fig()
# fitted_model.f2_evaluation()
# fitted_model.predict_image()

