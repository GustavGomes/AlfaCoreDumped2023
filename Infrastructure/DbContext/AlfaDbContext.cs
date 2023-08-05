using AlfaCoreDumped.Domain.Entities.CompanyResources;
using AlfaCoreDumped.Domain.Entities.ExternalCandidate;
using AlfaCoreDumped.Domain.Entities.ExternalReport;
using AlfaCoreDumped.Domain.Entities.InternalUser;
using AlfaCoreDumped.Domain.Entities.InternalUser.UserSolicitation;
using Microsoft.EntityFrameworkCore;

namespace AlfaCoreDumped.Infrastructure.DbContext
{
    public class AlfaDbContext : Microsoft.EntityFrameworkCore.DbContext
    {
        public AlfaDbContext(DbContextOptions<AlfaDbContext> options) : base(options) { }

        public DbSet<User> Users { get; set; }
        public DbSet<RescissionSolicitation> RescissionSolicitations { get; set; }
        public DbSet<VacationSolicitation> VacationSolicitation { get; set; }
        public DbSet<Report> Reports { get; set; }
        public DbSet<Candidate> Candidates { get; set; }
        public DbSet<Relative> Relatives { get; set; }
        public DbSet<Area> Areas { get; set; }
        public DbSet<Equipment> Equipments { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<User>()
                .HasMany(u => u.VacationSolicitations)
                .WithOne()
                .HasForeignKey(v => v.Id)
                .OnDelete(DeleteBehavior.Restrict);

            modelBuilder.Entity<User>()
                .HasMany(u => u.RescissionSolicitations)
                .WithOne()
                .HasForeignKey(r => r.Id)
                .OnDelete(DeleteBehavior.Restrict);
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<Area>().HasData(
                new Area()
                {
                    Id = Guid.Parse("d28888e9-2ba9-473a-a40f-e38cb54f9b35"),
                    Code = "Area1",
                    Description = "Descrição da area 1",
                    LiberationStatus = false,
                    PdfFile = new byte[]{1}
                }
            );
        }
    }
}
