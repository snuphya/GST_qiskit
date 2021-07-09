import pygsti

GST_type = "smq2Q_XYICPHASE"

data = pygsti.io.load_data_from_dir(GST_type)

#run the GST protocol and create a report 
gst_protocol = pygsti.protocols.StandardGST('TP,CPTP,Target')
results = gst_protocol.run(data)

report = pygsti.report.construct_standard_report(
    results, title="{} using qiskit".format(GST_type), verbosity=2)
report.write_html("{} using qiskit".format(GST_type), verbosity=2)