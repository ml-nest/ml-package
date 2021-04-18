def z_score(data, rqrd_col, thresh):
  """
  Intro
  ------
  Detects outliers based on the z score thresholds

  Params
  ------
  data(df) : DateFrame
  rqrd_col(str) : Column to be analysed
  thresh(float) : z value above which the output is considered as an outlier

  Returns
  -------
  Dataframe with additional two colmns one with z-score and other with label of outlier
  """
  z_mean = np.mean(data[rqrd_col])
  z_std = np.std(data[rqrd_col])

  df_z_outlier = data.copy()
  df_z_outlier['z_score']= (data[rqrd_col] - z_mean)/z_std
  label = []
  for i in df_z_outlier['z_score']:
    if abs(i) > thresh:
      label.append('Anomaly')
    else:
      label.append('Normal')
  df_z_outlier['outlier_flag'] = np.array(label)
  
  return df




#------------------------------------------------------Plots----------------------
def plot_zscore(df_z_outlier, enter_col, z_thresh):
  """
  Intro
  ------
  Plots a line density plot with vertical lines segmenting the outliers from normal datapoints

  Params
  ------
  df_z_outlier(df) : DateFrame with z-score and outlier flag
  enter_col(str) : Column to be analysed
  z_thresh(float) : z value above which the output is considered as an outlier
  """
  # scatter plot for column using z-score
  fig = go.Figure()
  fig = px.scatter(df_z_outlier, x="z_score", y=enter_col, 
                    opacity=0.5, color="outlier_flag")
  fig.data[0]['marker'].update(color='green')
  fig.data[1]['marker'].update(color='red')

  # plotting the threshold entered by the user
  fig.add_shape(type="line", x0=z_thresh, y0=0,
                x1=z_thresh, y1= max(df_z_outlier[enter_col]),
                line=dict(color="red", width=1, dash="dashdot"))

  fig.add_shape(type="line", x0=-z_thresh, y0=0,
                x1=-z_thresh, y1=max(df_z_outlier[enter_col]),
                line=dict(color="red",width=1,dash="dashdot"))

  fig.update_layout(title = "Scatter Plot of Z-Score vs `{}`".format(enter_col),
                    title_x = 0.5)
  fig.show()