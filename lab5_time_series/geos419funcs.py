import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from obspy import UTCDateTime


def plot_waveforms(st, st_2=None, marks=None, fmt="absolute",
                   tick_every=None):
    """
    Generic Obspy Stream waveform plotter for use in GEOS419 Time Series Lab
    :type st: obspy.core.stream.Stream
    :param st: Stream object to plot
    :type st_2: obspy.core.stream.Stream
    :param st_2: Optional second stream to plot together with `st` on the same axis
    :type marks: list of str
    :param marks: put a vertical line at all UTC times listed
    :type fmt: str
    :param fmt: x-axis label formatter, 'absolute' for timestamps, 'relative' for starttime t=0
    """
    f, axs = plt.subplots(len(st), figsize=(10, 8), sharex=True, sharey=True)
    if len(st) == 1:
        axs = [axs]
    plt.subplots_adjust(hspace=0.025)
    
    # X-axis formatting
    if fmt == "absolute":
        time_format = "matplotlib"
        axs[-1].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S.%f"))  # %H:%M:%S.%f
        axs[-1].tick_params(axis="x", labelrotation=20)
        if tick_every:
            axs[-1].xaxis.set_major_locator(mdates.MinuteLocator(interval=tick_every))
    else:
        time_format = "relative"

    # Make copies so we can sort the waveforms in-place
    st_plot = st.copy()
    st_plot.sort()
    time = st_plot[0].times(time_format)  # assuming all have the same time axis
    
    # Determine what to do if we plot two waveforms or just one
    if st_2 is None:
        st_2_plot = [None for _ in range(len(st))]
        alpha = 1
    else:
        st_2_plot = st_2.copy()
        st_2_plot.sort()
        time_2 = st_2_plot[0].times(time_format)
        alpha = 0.8
    
    # Loop through each trace and plot
    for i, (tr, tr_2) in enumerate(zip(st_plot, st_2_plot)):
        axs[i].plot(time, tr.data, label=tr.get_id(), c="k", lw=0.75,
                    zorder=10, alpha=alpha)
        # Plot the second set of waveforms below and slightly transparent 
        if tr_2:
            axs[i].plot(time_2, tr_2.data, label=tr_2.get_id(), c="r", lw=0.75,
                        zorder=9, alpha=0.75)
            
        axs[i].legend(loc="upper right", frameon=False)
        axs[i].grid()

    if marks:
        if fmt == "absolute":
            for mark in marks:
                m = UTCDateTime(mark).matplotlib_date
                axs[0].axvline(m, c="r", alpha=0.5)
        else:
            for mark in marks:
                m = UTCDateTime(mark) - time[0]  # relative time
                axs[0].axvline(m, c="r", alpha=0.5)
                
    # General Plot Aesthetics
    axs[0].set_title(f"{st[0].stats.starttime} - {st[0].stats.endtime}")
    axs[-1].set_xlabel("Time [s]")
    axs[int((len(st)-1)/2)].set_ylabel("Amplitude")
    plt.xlim([time.min(), time.max()])
    
    plt.show()